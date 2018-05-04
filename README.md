Thumbor Focus Filter
===

This plugins provide a way to generate text via Thumbor Filter.

## Installation
`pip install thumbor_focus_filter`

## Configuration

By adding `FILTERS` in `thumbor.conf` with `thumbor_focus_filter`, for example:
```
FILTERS =     [
    # other filters....
    'thumbor_focus_filter',
]
```

## Usage
Add `focus()` to thumbor url at `filters` section, method signature is like this:

`focus(percentage_width,percentage_height)`

Here'are some examples:
```
http://thumbor/unsafe/filter:focus(49,32)/your-image-url
```
