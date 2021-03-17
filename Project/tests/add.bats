load harness

@test "add-1" {
  check '2 + 3' '5'
}

@test "add-2" {
  check '3 + 92' '95'
}

@test "add-3" {
  check '100 + 0' '100'
}

@test "add-4" {
  check '-1 + -3' '-4'
}

@test "add-5" {
  check '10 + -3' '7'
}

@test "add-6" {
  check '-1 + 0' '-1'
}

@test "add-7" {
  check '99 + 3 + 12 + 2' '116'
}

@test "add-8" {
  check '2 + 3 + 4 + -1' '8'
}

@test "add-9" {
  check '-1 + -2 + 3' '0'
}

@test "add-10" {
  check '-1 + -5 + -1' '-7'
}
