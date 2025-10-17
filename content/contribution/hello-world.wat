(module
  (import "env" "print" (func $print (param i32)))
  (memory (export "memory") 1)
  (data (i32.const 0) "Hello, World!\00")
  (func (export "main")
    i32.const 0
    call $print))
