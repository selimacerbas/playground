# Flowcharts
```mermaid
flowchart
    A[start]; B[car]; C[Cool];
    A --> B
    A --> C & D


```
# Chat Orientations
```mermaid
flowchart BT
    A[start]; B[car]; C[Cool];
    A --> B
    A --> C & D


```

# Node texts

```mermaid
flowchart
    A["A:family"];
    B["`B:__Man__ 'Nice'`"];
    C[C:Woman];

    A --> B
    A --> C & D[D:Children]

```

# Links
```mermaid
flowchart
    A o--o B
    A -.-> B
    A -.- B
    A ==> B
    A --ref--> B
    C -->|text| D
    E ~~~ F
    T ~~~|invinsible| Z

```

# Advanced Links
```mermaid
flowchart
    A & B --> C & D
    E -->|text| F -->|text2| G -->|text3| E



```

# Real world example

```mermaid
flowchart
    A([Start]) --> B[/Input x/]
    B --> C{x > 5?}
    C -->|yes|D((stop))
    C -->|no|E[/print x/]
    E --> F[x = x + 1]
    F --> C


```
# Subgraphs

```mermaid
flowchart
    subgraph one[cool]
        direction LR
        A --> B
    end
    
    subgraph two 
        one --> two
    end

    subgraph three
        direction RL
        subgraph four
            direction BT
            C --> D & E
        end
    end


```

# Styling Lines and Nodes

```mermaid

%%{init: {"flowchart": {"curve": "stepAfter"}}}%%

flowchart TD
    A([Start]) --> B[/Input x/]
    B --> C{x > 5?}
    C -->|yes|D((stop))
    C -->|no|E[/print x/]
    E --> F[x = x + 1]
    F --> C

```

# Real World Kubernetes

```mermaid
flowchart LR
  %% Orientation: LR (left→right). Use TD for top→down.

  subgraph Internet
    user[User]
  end

  subgraph Cluster["Kubernetes Cluster"]
    direction LR

    subgraph nsProd["Namespace: prod"]
      ingress[Ingress Controller]
      svc[Service]
      subgraph app["Deployment: web (pods)"]
        pod1[(Pod)]
        pod2[(Pod)]
      end
      db[(Postgres PVC)]
      np{{NetworkPolicy: default-deny}}
      rbac[[RBAC: least privilege]]
    end

    subgraph nsSec["Namespace: security"]
      falco[DaemonSet: Falco]
    end
  end

  user -->|TLS| ingress --> svc --> app
  app -->|5432| db
  falco -.tap.-> app
  np -.enforces.-> app
  rbac -.enforces.-> app

  classDef boundary stroke:#f66,stroke-width:2px,stroke-dasharray:6 4,fill:#fff;
  class Cluster,nsProd,nsSec boundary;
```

```mermaid
sequenceDiagram
  autonumber
  actor U as User
  participant GW as API Gateway
  participant OR as Orchestrator/Router
  participant V as Vector DB
  participant LLM as LLM
  participant A as Tool-Using Agent
  participant S as External Service

  U->>GW: Query
  GW->>OR: Request + policy
  OR->>V: Embed & search
  V-->>OR: Top-K context
  OR->>LLM: Prompt + context
  LLM-->>OR: Plan + tool calls
  OR->>A: Execute(plan)
  A->>S: API call
  S-->>A: Result
  A-->>OR: Tool output
  OR->>LLM: Ground & compose
  LLM-->>GW: Final answer
  Note over OR,VLLM: Guardrails (PII, rate limits, red-teaming)


```

```mermaid
flowchart LR
  commit[Commit] --> ci[CI: build & test]
  ci --> image[Build container image]
  image --> scan[Security scan]
  scan --> registry[(Image Registry)]
  registry --> train[(Train job K8s)]
  train -->|metrics| mlmd[(ML Metadata Store)]
  train --> model[Model artifact]
  model --> eval[Offline evaluation]
  eval --> gate{Quality gate}
  gate -- pass --> deploy[Deploy to prod]
  gate -- fail --> iterate[Iterate]
  deploy --> monitor[Online monitoring]
  monitor --> drift{Drift detected?}
  drift -- yes --> retrain[Trigger retraining]


```

# C4 Modelling

## C1
1) C1 (System Context) → Mermaid Flowchart
Boxes = people/systems; one box = “Your System”.
Edges = relationships (with short purpose labels).
```mermaid
flowchart LR
  classDef person fill:#eef,border:1px solid #99f,stroke:#99f;
  classDef system fill:#efe,stroke:#6c6;
  classDef yours fill:#ffd,stroke:#cc0,stroke-width:2px;

  U[Person: End User]:::person -->|Uses| YS[Your System]:::yours
  ExtA[External System A]:::system -->|Webhook| YS
  YS -->|API| ExtB[External System B]:::system
```

## C2
2) C2 (Container) → Mermaid Flowchart + subgraphs
Subgraph = your system boundary.
Nodes inside = containers (web, API, DB, queue, jobs, vector DB, etc).
Great for Kubernetes, MLOps, agentic AI building blocks.
```mermaid
flowchart LR
  subgraph YS["Your System (C2: Containers)"]
    Web[Web App]
    API[API Service]
    Worker[Async Worker]
    DB[(Relational DB)]
    Vec[(Vector DB)]
    Q[[Message Queue]]
  end
  User[User] --> Web --> API
  API --> DB
  API --> Vec
  API --> Q --> Worker

```

## C3
3) C3 (Component) → Mermaid Flowchart (zoom into one container)
Pick one container (e.g., API Service) and show main components.
```mermaid
flowchart TD
  subgraph API["API Service (C3: Components)"]
    Ctrl[Controllers]
    Svc[Domain Services]
    Repo[Repositories]
    Adap[Integrations/Adapters]
  end
  Ctrl --> Svc --> Repo
  Svc --> Adap


```

## C4
4) Dynamic view (C4 “Dynamic”) → Mermaid Sequence
Show runtime calls for a specific use case (e.g., agent planning + tool calls).
```mermaid
sequenceDiagram
  actor U as User
  participant Web
  participant API
  participant Agent
  participant Vec as Vector DB
  participant LLM
  U->>Web: Query
  Web->>API: HTTP POST /ask
  API->>Vec: Semantic search
  Vec-->>API: Top-K results
  API->>LLM: Prompt + context
  LLM-->>API: Plan + tool call
  API->>Agent: Execute(tool)
  Agent-->>API: Result
  API-->>Web: Response

```
