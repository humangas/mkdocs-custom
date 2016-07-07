# [js-sequence-diagrams](https://bramp.github.io/js-sequence-diagrams/)
- [source code](https://raw.githubusercontent.com/humangas/mkdocs-custom/master/docs/js-sequence-diagrams.md)

<script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.2.1/raphael.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/js-sequence-diagrams/1.0.6/sequence-diagram-min.js"></script>

<div class="diagram">
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
</div>

<script>
$(".diagram").sequenceDiagram({theme: 'simple'});
</script>
