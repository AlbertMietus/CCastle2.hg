.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.?

CCastle Package Architecture
===========================

.. contents:: Table of Contents
   :local:
   :depth: 2

Core Architecture (Main Packages)
---------------------------------

The CCastle project is organized in a **3-layer hierarchy**:

.. uml::
   :align: center
   :caption: Main Package Dependencies

   @startuml
   !define CATEGORY_COLOR_BASE #E1F5FF
   !define CATEGORY_COLOR_CORE #FFF3E0

   skinparam backgroundColor #FAFAFA
   skinparam ArrowColor #424242
   skinparam ArrowThickness 2

   rectangle "📦 BASE PACKAGES" #E1F5FF {
       component "castle-monorail\n[v0.0.2]\nVisitor Pattern" as mono
       component "castle-aigr\n[v0.0.5]\nAbstract IR" as aigr
       component "castle-aigr-trawlers\n[v0.0.1]\nTree Tools" as trawlers
   }

   rectangle "🔧 CORE PACKAGES" #FFF3E0 {
       component "castle-TatSu-reader\n[v0.0.1]\nParser" as reader
       component "castle-RPy-writer\n[v0.0.1]\nCode Gen" as writer
   }

   mono -down-> "" : (foundation)
   aigr -down-> mono: depends
   trawlers -down-> aigr: depends
   reader -down-> aigr: depends
   writer -down-> aigr: depends
   writer -down-> mono: uses Visitor

   @enduml

**Base Packages (Foundation)**

- **castle-monorail** [v0.0.2]

  - *Role:* Foundation layer providing visitor pattern & dispatch mechanisms
  - *Dependencies:* None
  - *Key exports:* Visitor, dispatch utilities

- **castle-aigr** [v0.0.5]

  - *Role:* Abstract Intermediate Representation (IR) for the language
  - *Dependencies:* castle-monorail
  - *Key exports:* AIGR classes, node types, protocol definitions

- **castle-aigr-trawlers** [v0.0.1]

  - *Role:* Tree traversal tools and utilities for AIGR
  - *Dependencies:* castle-aigr
  - *Key exports:* Trawler utilities, tree navigation tools

**Core Packages (Processing)**

- **castle-TatSu-reader** [v0.0.1]

  - *Role:* Parser - converts source code to AIGR
  - *Dependencies:* castle-aigr
  - *Key exports:* Parsing functions, AST→AIGR conversion

- **castle-RPy-writer** [v0.0.1]

  - *Role:* Code generator - converts AIGR to Python/RPy output
  - *Dependencies:* castle-aigr, castle-monorail
  - *Key exports:* Code generation, rendering functions

Complete Architecture (Including Test Doubles)
----------------------------------------------

.. uml::
   :align: center
   :caption: Full Dependency Graph with Test Fixtures

   @startuml
   skinparam backgroundColor #FAFAFA
   skinparam ArrowColor #424242
   skinparam ArrowThickness 2

   rectangle "📦 BASE PACKAGES" #E1F5FF {
       component "castle-monorail\n[v0.0.2]" as mono
       component "castle-aigr\n[v0.0.5]" as aigr
       component "castle-aigr-trawlers\n[v0.0.1]" as trawlers
   }

   rectangle "🔧 CORE PACKAGES" #FFF3E0 {
       component "castle-TatSu-reader\n[v0.0.1]" as reader
       component "castle-RPy-writer\n[v0.0.1]" as writer
   }

   rectangle "🧪 TEST DOUBLES" #F3E5F5 {
       component "TestDoubles-aigr-base\n[fixture]" as td_base
       component "TestDoubles-aigr-sieve\n[fixture]" as td_sieve
       component "TestDoubles-HelloWorlds\n[fixture]" as td_hello
   }

   mono -down-> "" : (foundation)
   aigr -down-> mono: depends
   trawlers -down-> aigr: depends
   reader -down-> aigr: depends
   writer -down-> aigr: depends
   writer -down-> mono: uses

   td_base -down-> aigr: uses
   td_sieve -down-> aigr: uses
   td_sieve -down-> td_base: uses
   td_hello -down-> aigr: uses

   @enduml

**Test Double Packages** (🧪)

- **TestDoubles-aigr-base** [fixture]

  - *Role:* Base test fixtures for AIGR testing
  - *Dependencies:* castle-aigr
  - *Usage:* Unit tests for aigr functionality

- **TestDoubles-aigr-sieve** [fixture]

  - *Role:* Test fixtures for protocol/namespace filtering
  - *Dependencies:* castle-aigr, TestDoubles-aigr-base
  - *Usage:* Tests for component sieving and filtering

- **TestDoubles-HelloWorlds** [fixture]

  - *Role:* Example programs for end-to-end testing
  - *Dependencies:* castle-aigr
  - *Usage:* Integration tests, code generation validation

Dependency Summary
------------------

.. list-table:: Package Dependencies Matrix
   :header-rows: 1
   :widths: 25 50 25

   * - Package
     - Dependencies
     - Category
   * - castle-monorail
     - *(none)*
     - Base
   * - castle-aigr
     - castle-monorail
     - Base
   * - castle-aigr-trawlers
     - castle-aigr
     - Base
   * - castle-TatSu-reader
     - castle-aigr
     - Core
   * - castle-RPy-writer
     - castle-aigr, castle-monorail
     - Core
   * - TestDoubles-aigr-base
     - castle-aigr
     - Test
   * - TestDoubles-aigr-sieve
     - castle-aigr, TestDoubles-aigr-base
     - Test
   * - TestDoubles-HelloWorlds
     - castle-aigr
     - Test

Key Design Principles
---------------------

1. **Layered Architecture**: Clean separation between foundation (monorail), abstraction (aigr), and tools
2. **Single Responsibility**: Each package has a focused purpose (parsing, generation, testing)
3. **Explicit Dependencies**: All internal dependencies are declared in ``pyproject.toml``
4. **Version Consistency**: All packages at v0.0.x indicate experimental/early-stage development

.. note::
   **Important:** RPy-writer requires both ``castle-aigr`` and ``castle-monorail``
   (for the Visitor pattern). This direct dependency on monorail is intentional and explicit.
