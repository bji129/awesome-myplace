Title: Python Markdown
Date: 2022-07-28 10:03
Modified: 2022-07-28 10:03
Category: news
Tags: markdown, learn, python
Authors: Brandon Ji
Summary: Python-Markdown is almost completely compliant with the reference implementation, though there are a few known issues.. 

[Python-Markdown][]
===================
This is a Python implementation of John Gruber's [Markdown][].
It is almost completely compliant with the reference implementation,
though there are a few known issues. See [Features][] for information
on what exactly is supported and what is not. Additional features are
supported by the [Available Extensions][].

[Python-Markdown]: https://Python-Markdown.github.io/
[Markdown]: https://daringfireball.net/projects/markdown/
[Features]: https://Python-Markdown.github.io#Features
[Available Extensions]: https://Python-Markdown.github.io/extensions

Documentation
-------------

```bash
pip install markdown
```
```python
import markdown
html = markdown.markdown(your_text_string)
```

For more advanced [installation] and [usage] documentation, see the `docs/` directory
of the distribution or the project website at <https://Python-Markdown.github.io/>.

[installation]: https://python-markdown.github.io/install/
[usage]: https://python-markdown.github.io/reference/

See the change log at <https://Python-Markdown.github.io/change_log>.

Support
-------

You may report bugs, ask for help, and discuss various other issues on the [bug tracker][].

[bug tracker]: https://github.com/Python-Markdown/markdown/issues