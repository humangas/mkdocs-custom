# [Viz.js](http://mdaines.github.io/viz.js/)

<script src="https://cdnjs.cloudflare.com/ajax/libs/viz.js/0.0.3/viz.js"></script>

<div id="diagram"></div>

<script id="digraph">
digraph "unix" {
  A [tooltip="ツールチップ"]
  A -> B;
  あ -> A;
}
</script>

<script>
//document.getElementById("diagram").innerHTML = Viz(document.getElementById('digraph').innerHTML, 'svg');
$("#diagram").html(Viz(document.getElementById('digraph').innerHTML, 'svg'));
</script>
