# [Flowchart.js](http://flowchart.js.org)
- [source code](https://raw.githubusercontent.com/humangas/mkdocs-custom/master/docs/flowchartjs.md)

<script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.2.1/raphael.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/flowchart/1.6.3/flowchart.min.js"></script>
<script src ="jquery-plugin.js"></script>

<div class="diagram">
st=>start: Start|past:>http://www.google.com[blank]
e=>end: Ende|future:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|future

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2->e
</div>

<script>
$(".diagram").flowchart();
</script>
