datatype Tree<T> = Leaf | Node(Tree<T>, Tree<T>, T)
datatype List<T> = Nil | Cons(T, List<T>)

function flatten<T>(tree:Tree<T>):List<T>
{
  match tree
    case Leaf => Nil
    case Node(t1, t2, t) => Cons(t, append(flatten(t1), flatten(t2)))
}




function append<T>(xs:List<T>, ys:List<T>):List<T>
ensures xs == Nil ==> append(xs,ys) == ys
ensures ys == Nil ==> append(xs,ys) == xs
// ensures length(append(xs,ys)) == length(xs) + length(ys)
{
  match xs
    case Nil => ys
    case Cons(x, tail) => Cons(x,append(tail,ys))
}




function treeContains<T>(tree:Tree<T>, element:T):bool
{
	match tree
    case Leaf => false
    case Node(t1, t2, t) => t == element || treeContains(t1, element) || treeContains(t2, element)
}




function listContains<T>(xs:List<T>, element:T):bool
{
  match xs
    case Nil => false
    case Cons(y, tail) => y == element || listContains(tail, element)
}




lemma sameElements<T>(tree:Tree<T>, element:T)
ensures treeContains(tree, element) <==> listContains(flatten(tree), element)
ensures treeContains(tree, element) == listContains(flatten(tree), element)
ensures listContains(flatten(tree), element) == treeContains(tree, element)
decreases tree
{
	match tree
    case Leaf => {}
    case Node(t1, t2, t) => calc {
      //treeContains(tree, element) == listContains(flatten(tree), element);
      //listContains(flatten(tree), element) == treeContains(tree, element);
      sameElements(t1, element);
      assert treeContains(t1, element) 
          == treeContains(Node(t1', t2', t'), element)
          == treeContains(Cons(t', append(flatten(t1'), flatten(t2'))), element)

      ;
      // assert listContains(flatten(tree), element) 
      //     == listContains(flatten(Node(t1, t2, t)), element)
      // ;
      
      // treeContains(tree, element) == listContains(flatten(tree),element) && listContains(flatten(tree), element) == treeContains(tree, element);
      }
}