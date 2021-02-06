load harness

@test "myown-1" {
  check 'x := -3' '⇒ skip, {x → -3}'
}

@test "myown-2" {
  check 'if x = 0 ∧ y < 4 then x := 5 else x := 2' '⇒ x := 5, {}
⇒ skip, {x → 5}'
}

@test "myown-3" {
  check 'while false do x := 1' '⇒ skip, {}'
}

@test "myown-4" {
  check 'z := 15 ; { a := 5 ; b := 4 ; c := 3 }' '⇒ skip; a := 5; b := 4; c := 3, {z → 15}
⇒ a := 5; b := 4; c := 3, {z → 15}
⇒ skip; b := 4; c := 3, {a → 5, z → 15}
⇒ b := 4; c := 3, {a → 5, z → 15}
⇒ skip; c := 3, {a → 5, b → 4, z → 15}
⇒ c := 3, {a → 5, b → 4, z → 15}
⇒ skip, {a → 5, b → 4, c → 3, z → 15}'
}

@test "myown-5" {
  check 'i := 10 ; j := 5 ; if true then n := i / j else n := i' '⇒ skip; j := 5; if true then { n := (i/j) } else { n := i }, {i → 10}
⇒ j := 5; if true then { n := (i/j) } else { n := i }, {i → 10}
⇒ skip; if true then { n := (i/j) } else { n := i }, {i → 10, j → 5}
⇒ if true then { n := (i/j) } else { n := i }, {i → 10, j → 5}
⇒ n := (i/j), {i → 10, j → 5}
⇒ skip, {i → 10, j → 5, n → 2}'
}