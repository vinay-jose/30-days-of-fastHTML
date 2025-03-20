**Prompt:**
```
Now please create a similar table for code defined in the cells that are not exported. Add one more column to indicate whether they are in a hidden cell or not.
```

Let me create a table for the non-exported code in the notebook:

| # | Name | Type | Purpose | Hidden | Notes |
|---|------|------|---------|--------|-------|
| 1 | `Markdown` | Import | From IPython.display for markdown display | No | Used for notebook display |
| 2 | `pprint` | Import | From pprint for pretty printing | No | Used for debugging |
| 3 | `test_eq` | Import | From fastcore.test for testing | No | Used for testing functions |
| 4 | `samp` | Variable | Example HTML structure | No | Demonstration variable |
| 5 | `elem` | Variable | Example P element | No | Demonstration variable |
| 6 | `PageTitle` | Class | Example class with __ft__ method | No | Shows custom class integration |
| 7 | `HomePage` | Class | Example class with __ft__ method | No | Shows nested custom class integration |
| 8 | `h` | Variable | Result of to_xml(samp) | No | Demonstration variable |
| 9 | `h` (second) | Variable | Result of to_xml with indent=False | No | Demonstration variable |
| 10 | `_esc` | Function | Example escape function | No | Demonstrates interoperability |
| 11 | `r` | Variable | Example Safe string | No | Used in interoperability demo |
| 12 | Various test cases | Code | Tests for to_xml function | Yes | Hidden in `#| hide` cells |

The notebook contains several examples and demonstrations that show how to use the library's functionality. There are also hidden test cells (marked with `#| hide`) that contain test cases to verify the functionality works correctly.
