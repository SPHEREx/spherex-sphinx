# Test SPHEREx Technote

```{abstract}
The abstract is a brief summary of the document. In technotes it is specially marked up with an `abstract` directive.
```

## Introduction

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac purus sit amet nunc maximus ultricies. Nullam nec magna nec nuncegestas tincidunt ut ac justo. {cite}`SPHEREx_SPIE`

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.

## Images and figures

A figure with a caption:

```{figure} https://placehold.co/400x400

A placeholder image.
```

### Wide figures

A figure marked with the `technote-wide-content` class applied as a `figclass` option:

```{figure} https://placehold.co/1200x400
:figclass: technote-wide-content

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.
```

## Tables

A table:

```{list-table}
:header-rows: 1

* - Column 1
  - Column 2
  - Column 3
* - Row 1
  - 1
  - 1
* - Row 2
  - 2
  - 2
* - Row 3
  - 3
  - 3
```

A table marked with the `technote-wide-content` class:

```{rst-class} technote-wide-content

```

```{list-table}
:header-rows: 1

* - Column 1
  - Column 2
  - Column 3
  - Column 4
  - Column 5
  - Column 6
  - Column 7
* - Row 1
  - lorem ipsum dolor sit amet consectetur adipiscing elit
  - lorem ipsum dolor
  - lorem ipsum dolor
  - 5
  - 6
  - Lorem ipsum
* - Row 2
  - 6
  - 7
  - 8
  - 9
  - 10
  - Lorem ipsum
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.

## Code blocks

A regular code block:

```{code-block} python
print("Hello, world!")
```

And with a caption:

```{code-block} python
:caption: A code block with a caption

print("Hello, world!")
```

A wide code block without a caption:

```{rst-class} technote-wide-content

```

```{code-block} python
print("Hello, world! This is a code block. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.")
```

A wide code block with a caption where the class is set externally:

```{rst-class} technote-wide-content

```

```{code-block} python
:caption: A wide code block. This is a long caption. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.

print("Hello, world! This is a code block. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.")
```

## Admonitions

An admonition:

```{note}
This is a note. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.
```

## Lists

A bulleted list:

- Item 1
- Item 2
- Item 3

A numbered list:

1. Item 1
2. Item 2
3. Item 3

A bulleted list with a nested numbered list:

- Item 1
  1. Item 1.1
  2. Item 1.2
- Item 2
- Item 3

A definition list:

term 1
: Definition 1

term 2
: Definition 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl quis molestie ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.

## References

```{bibliography}

```
