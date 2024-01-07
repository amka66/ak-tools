# Setting up a Lean4 development environment

Author: Amir Kantor  
Updated: Jan 2024

First, install `elan` (which handles installations of multiple versions of lean, and its package manager `lake`, and handles the installation of updates) per the tool's installation instructions.

## Updating `elan` and `lean`:

Update elan (lean toolchain installer):

```
elan self update
```

Update lean:

```
elan toolchain install stable
```

Set the updated lean version as default:

```
elan default stable
```

## New lean project (aka, lean package)

To initialize a lean project in the current directory (library and executable):

```
lake init .
```

And for a dependency on mathlib4 use (apparently it creates a library with no executable):

```
lake init . math
```

Then, update the dependencies via:

```
lake update
```

Then, build an executable and run it via:

```
lake exe cache get
```

To test that the new project is properly set, create a file `Test.lean` under the main Lean package folder (e.g., `my_project/MyProject/`) including:

```
import Mathlib.Topology.Basic

#check TopologicalSpace
```

When the cursor is on the last line, the right hand part of VS Code should display a "Lean Infoview" area saying: `TopologicalSpace.{u} (α : Type u) : Type u.`
