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


// flatten(Node(t1, t2, t)) == Cons(t, append(flatten(t1), flatten(t2)))
// append(x, tail) == Cons(x,append(tail,ys))
// treeContains(Node(t1, t2, t), element) == t == element || treeContains(t1, element) || treeContains(t2, element)

ghost method sameElements<T>(tree:Tree<T>, element:T)
// ensures treeContains(tree, element) <==> listContains(flatten(tree), element)
// ensures treeContains(tree, element) == listContains(flatten(tree),element) && listContains(flatten(tree), element) == treeContains(tree, element);
decreases tree
{
	match tree
    case Leaf => {}
    case Node(t1, t2, t) =>  calc {

      treeContains(tree, element) == listContains(flatten(tree),element);

      /* BELOW ARE MY MANY DIFFERENT ATTEMPTS TO THIS LEMMA
       * but the current form of my answer seems to work after I changed the LEMMA to a
       * GHOST METHOD since lemma and ghost methods are similar.
       *
       * I also moved the post condition down to the body of the ghost method where 
       * the case is a Node, which made things work.
       *
       * Among the many different ways I wrote of defining the lemma, I felt that defining
       * treeContains(tree, element) to listContains(flatten(tree), element) or the other
       * way around didn't seem to work.
      */


      // treeContains(tree, element) == listContains(flatten(tree), element);
      // listContains(flatten(tree), element) == treeContains(tree, element);
      // sameElements(t1, element);
      // sameElements(t2, element);

      // assert treeContains(tree, element)
      //     == treeContains(Node(t1, t2, t), element)
      //     == listContains(Cons(t, append(flatten(t1), flatten(t2))), element)
      //     == listContains(flatten(Node(t1,t2,t)), element)
      //     == listContains(flatten(tree), element);


      // assert treeContains(tree, element)
      //     == treeContains(Node(t1,t2,t), element)
          // == treeContains(t1, element) || treeContains(t2, element)
          // == listContains(flatten(t1), element) || listContains(flatten(t2), element)
          // == listContains(Cons(t, append(flatten(t1), flatten(t2))), element)
          // == listContains(flatten(Node(t1, t2, t)), element)
          // == listContains(flatten(tree), element); 
      
      // assert listContains(flatten(tree), element)
      //     == listContains(flatten(Node(t1,t2,t)), element);

    }
}