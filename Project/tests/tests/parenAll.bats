load harness

@test "parenAll-1" {
  check '( 8 - 2 ) * 5' '30'
}

@test "parenAll-2" {
  check '( 2 + 9 ) * 9' '99'
}

@test "parenAll-3" {
  check '5 * ( 4 - 3 )' '5'
}

@test "parenAll-4" {
  check '( 5 + 5 ) / 5' '2'
}

@test "parenAll-5" {
  check '( 7 + 9 - 6 ) * 5' '50'
}

@test "parenAll-6" {
  check '( 1 + 4 ) * 2' '10'
}

@test "parenAll-7" {
  check '( -12 - 4 ) / 4' '-4'
}

@test "parenAll-8" {
  check '( 4 - 9 ) + 2' '-3'
}

@test "parenAll-9" {
  check '( 4 * 3 ) - 2 / 2' '11'
}

@test "parenAll-10" {
  check '( 49 - 3 ) * 2' '92'
}