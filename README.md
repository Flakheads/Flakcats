# Flakcats
A hybrid of Brain-Flak and Stack Cats.

---

## How it works

flackcats like Brain-Flak has two stacks and consists of only balanced parentheses.  Like Stack Cats, flakcats programs cannot
have a mirror symmetry and are reversable.

### The Operations

- `()` does nothing and evaluates as 1 (*same as Brain-Flak*)

- `[]` does nothing and evaluates as -1 (*same as Brain-Flak Classic*)

- `<>` switches the active stack and evaluates as 0 (*same as Brain-Flak*)

- `{}` swaps the top two values and evaluates as their sum

- `(...)` pops the top of the current stack evaluates the inside and then pushes the result minus the popped value

- `[...]` evaluates as the negative of the inside (*same as Brain-Flak*)

- `<...>` evaluates as zero regardless of the inside (*same as Brain-Flak*)

- `{...}` remembers the top of the stack and runs the code inside until the top of stack is the same as the remembered value (*same as Stack Cats*)
