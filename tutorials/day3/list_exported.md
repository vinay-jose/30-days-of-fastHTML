| # | Name | Type | Purpose | Importance |
|---|------|------|---------|------------|
| 1 | `_fix_k()` | Utility Function | Fixes key names for attributes by handling underscores and dashes | Medium |
| 2 | `_specials` | Global Variable | Set of special characters used in attribute mapping | Medium |
| 3 | `attrmap()` | Utility Function | Maps attribute names to their HTML equivalents | Medium |
| 4 | `valmap()` | Utility Function | Transforms values for attributes (lists, dicts, etc.) | Medium |
| 5 | `_flatten_tuple()` | Utility Function | Flattens nested tuples into a single tuple | Medium |
| 6 | `_preproc()` | Utility Function | Preprocesses children and keyword arguments | Medium |
| 7 | `FT` | Class | Core "Fast Tag" class representing XML/HTML elements | High |
| 8 | `ft()` | Function | Creates an FT structure | High |
| 9 | `voids` | Global Variable | Set of HTML void element tags | Medium |
| 10 | `_g` | Global Variable | Reference to the global namespace dictionary | Medium |
| 11 | `_all_` | Global Variable | List of HTML tag names exported as functions | Medium |
| 12 | HTML Tag Functions | Generated Functions | Convenience functions for creating HTML elements (Div, P, etc.) | High |
| 13 | `Html()` | Function | Special function for creating HTML documents with optional doctype | High |
| 14 | `Safe` | Class | String subclass that doesn't get escaped in HTML output | Medium |
| 15 | `_escape()` | Utility Function | Handles escaping of strings | Medium |
| 16 | `_noescape()` | Utility Function | Skip escaping of strings | Medium |
| 17 | `_to_attr()` | Utility Function | Converts attribute key-value pairs to strings | Medium |
| 18 | `_block_tags` | Global Variable | Set of HTML block-level tags | Medium |
| 19 | `_inline_tags` | Global Variable | Set of HTML inline tags | Medium |
| 20 | `_is_whitespace_significant()` | Utility Function | Determines if whitespace is significant in an element | Medium |
| 21 | `_to_xml()` | Utility Function | Internal function to convert FT elements to XML | High |
| 22 | `to_xml()` | Function | Converts FT elements to XML/HTML strings | High |
| 23 | `highlight()` | Function | Formats XML as markdown for syntax highlighting | Low |
| 24 | `showtags()` | Function | Shows XML tags in a preformatted code block | Low |
| 25 | `__getattr__()` | Function | Module-level function for dynamically creating tag functions | Medium |
