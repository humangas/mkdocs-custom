# [mermaid](http://knsv.github.io/mermaid/#mermaid)
- [source code](https://raw.githubusercontent.com/humangas/mkdocs-custom/master/docs/mermaid.md)

<!--
<link href="https://cdnjs.cloudflare.com/ajax/libs/mermaid/6.0.0/mermaid.dark.min.css" rel="stylesheet" type="text/css" />
<link href="https://cdnjs.cloudflare.com/ajax/libs/mermaid/6.0.0/mermaid.forest.min.css" rel="stylesheet" type="text/css" />
-->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mermaid/6.0.0/mermaid.min.css" rel="stylesheet" type="text/css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/6.0.0/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>

<div class="mermaid">
graph TB
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
</div>
