(define (problem visitall_17)
  (:domain visitall)
  (:objects 
    r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 - row
    c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13 c14 c15 c16 c17 - column)
  (:init
    (at_row r1)
    (at_column c1)
    (connected_rows r1 r2)
    (connected_rows r2 r3)
    (connected_rows r3 r4)
    (connected_rows r4 r5)
    (connected_rows r5 r6)
    (connected_rows r6 r7)
    (connected_rows r7 r8)
    (connected_rows r8 r9)
    (connected_rows r9 r10)
    (connected_rows r10 r11)
    (connected_rows r11 r12)
    (connected_rows r12 r13)
    (connected_rows r13 r14)
    (connected_rows r14 r15)
    (connected_rows r15 r16)
    (connected_rows r16 r17)
    (connected_columns c1 c2)
    (connected_columns c2 c3)
    (connected_columns c3 c4)
    (connected_columns c4 c5)
    (connected_columns c5 c6)
    (connected_columns c6 c7)
    (connected_columns c7 c8)
    (connected_columns c8 c9)
    (connected_columns c9 c10)
    (connected_columns c10 c11)
    (connected_columns c11 c12)
    (connected_columns c12 c13)
    (connected_columns c13 c14)
    (connected_columns c14 c15)
    (connected_columns c15 c16)
    (connected_columns c16 c17)
  )
  (:goal (and
    (visited r1 c1)
    (visited r1 c2)
    (visited r1 c3)
    (visited r1 c4)
    (visited r1 c5)
    (visited r1 c6)
    (visited r1 c7)
    (visited r1 c8)
    (visited r1 c9)
    (visited r1 c10)
    (visited r1 c11)
    (visited r1 c12)
    (visited r1 c13)
    (visited r1 c14)
    (visited r1 c15)
    (visited r1 c16)
    (visited r1 c17)
    (visited r2 c1)
    (visited r2 c2)
    (visited r2 c3)
    (visited r2 c4)
    (visited r2 c5)
    (visited r2 c6)
    (visited r2 c7)
    (visited r2 c8)
    (visited r2 c9)
    (visited r2 c10)
    (visited r2 c11)
    (visited r2 c12)
    (visited r2 c13)
    (visited r2 c14)
    (visited r2 c15)
    (visited r2 c16)
    (visited r2 c17)
    (visited r3 c1)
    (visited r3 c2)
    (visited r3 c3)
    (visited r3 c4)
    (visited r3 c5)
    (visited r3 c6)
    (visited r3 c7)
    (visited r3 c8)
    (visited r3 c9)
    (visited r3 c10)
    (visited r3 c11)
    (visited r3 c12)
    (visited r3 c13)
    (visited r3 c14)
    (visited r3 c15)
    (visited r3 c16)
    (visited r3 c17)
    (visited r4 c1)
    (visited r4 c2)
    (visited r4 c3)
    (visited r4 c4)
    (visited r4 c5)
    (visited r4 c6)
    (visited r4 c7)
    (visited r4 c8)
    (visited r4 c9)
    (visited r4 c10)
    (visited r4 c11)
    (visited r4 c12)
    (visited r4 c13)
    (visited r4 c14)
    (visited r4 c15)
    (visited r4 c16)
    (visited r4 c17)
    (visited r5 c1)
    (visited r5 c2)
    (visited r5 c3)
    (visited r5 c4)
    (visited r5 c5)
    (visited r5 c6)
    (visited r5 c7)
    (visited r5 c8)
    (visited r5 c9)
    (visited r5 c10)
    (visited r5 c11)
    (visited r5 c12)
    (visited r5 c13)
    (visited r5 c14)
    (visited r5 c15)
    (visited r5 c16)
    (visited r5 c17)
    (visited r6 c1)
    (visited r6 c2)
    (visited r6 c3)
    (visited r6 c4)
    (visited r6 c5)
    (visited r6 c6)
    (visited r6 c7)
    (visited r6 c8)
    (visited r6 c9)
    (visited r6 c10)
    (visited r6 c11)
    (visited r6 c12)
    (visited r6 c13)
    (visited r6 c14)
    (visited r6 c15)
    (visited r6 c16)
    (visited r6 c17)
    (visited r7 c1)
    (visited r7 c2)
    (visited r7 c3)
    (visited r7 c4)
    (visited r7 c5)
    (visited r7 c6)
    (visited r7 c7)
    (visited r7 c8)
    (visited r7 c9)
    (visited r7 c10)
    (visited r7 c11)
    (visited r7 c12)
    (visited r7 c13)
    (visited r7 c14)
    (visited r7 c15)
    (visited r7 c16)
    (visited r7 c17)
    (visited r8 c1)
    (visited r8 c2)
    (visited r8 c3)
    (visited r8 c4)
    (visited r8 c5)
    (visited r8 c6)
    (visited r8 c7)
    (visited r8 c8)
    (visited r8 c9)
    (visited r8 c10)
    (visited r8 c11)
    (visited r8 c12)
    (visited r8 c13)
    (visited r8 c14)
    (visited r8 c15)
    (visited r8 c16)
    (visited r8 c17)
    (visited r9 c1)
    (visited r9 c2)
    (visited r9 c3)
    (visited r9 c4)
    (visited r9 c5)
    (visited r9 c6)
    (visited r9 c7)
    (visited r9 c8)
    (visited r9 c9)
    (visited r9 c10)
    (visited r9 c11)
    (visited r9 c12)
    (visited r9 c13)
    (visited r9 c14)
    (visited r9 c15)
    (visited r9 c16)
    (visited r9 c17)
    (visited r10 c1)
    (visited r10 c2)
    (visited r10 c3)
    (visited r10 c4)
    (visited r10 c5)
    (visited r10 c6)
    (visited r10 c7)
    (visited r10 c8)
    (visited r10 c9)
    (visited r10 c10)
    (visited r10 c11)
    (visited r10 c12)
    (visited r10 c13)
    (visited r10 c14)
    (visited r10 c15)
    (visited r10 c16)
    (visited r10 c17)
    (visited r11 c1)
    (visited r11 c2)
    (visited r11 c3)
    (visited r11 c4)
    (visited r11 c5)
    (visited r11 c6)
    (visited r11 c7)
    (visited r11 c8)
    (visited r11 c9)
    (visited r11 c10)
    (visited r11 c11)
    (visited r11 c12)
    (visited r11 c13)
    (visited r11 c14)
    (visited r11 c15)
    (visited r11 c16)
    (visited r11 c17)
    (visited r12 c1)
    (visited r12 c2)
    (visited r12 c3)
    (visited r12 c4)
    (visited r12 c5)
    (visited r12 c6)
    (visited r12 c7)
    (visited r12 c8)
    (visited r12 c9)
    (visited r12 c10)
    (visited r12 c11)
    (visited r12 c12)
    (visited r12 c13)
    (visited r12 c14)
    (visited r12 c15)
    (visited r12 c16)
    (visited r12 c17)
    (visited r13 c1)
    (visited r13 c2)
    (visited r13 c3)
    (visited r13 c4)
    (visited r13 c5)
    (visited r13 c6)
    (visited r13 c7)
    (visited r13 c8)
    (visited r13 c9)
    (visited r13 c10)
    (visited r13 c11)
    (visited r13 c12)
    (visited r13 c13)
    (visited r13 c14)
    (visited r13 c15)
    (visited r13 c16)
    (visited r13 c17)
    (visited r14 c1)
    (visited r14 c2)
    (visited r14 c3)
    (visited r14 c4)
    (visited r14 c5)
    (visited r14 c6)
    (visited r14 c7)
    (visited r14 c8)
    (visited r14 c9)
    (visited r14 c10)
    (visited r14 c11)
    (visited r14 c12)
    (visited r14 c13)
    (visited r14 c14)
    (visited r14 c15)
    (visited r14 c16)
    (visited r14 c17)
    (visited r15 c1)
    (visited r15 c2)
    (visited r15 c3)
    (visited r15 c4)
    (visited r15 c5)
    (visited r15 c6)
    (visited r15 c7)
    (visited r15 c8)
    (visited r15 c9)
    (visited r15 c10)
    (visited r15 c11)
    (visited r15 c12)
    (visited r15 c13)
    (visited r15 c14)
    (visited r15 c15)
    (visited r15 c16)
    (visited r15 c17)
    (visited r16 c1)
    (visited r16 c2)
    (visited r16 c3)
    (visited r16 c4)
    (visited r16 c5)
    (visited r16 c6)
    (visited r16 c7)
    (visited r16 c8)
    (visited r16 c9)
    (visited r16 c10)
    (visited r16 c11)
    (visited r16 c12)
    (visited r16 c13)
    (visited r16 c14)
    (visited r16 c15)
    (visited r16 c16)
    (visited r16 c17)
    (visited r17 c1)
    (visited r17 c2)
    (visited r17 c3)
    (visited r17 c4)
    (visited r17 c5)
    (visited r17 c6)
    (visited r17 c7)
    (visited r17 c8)
    (visited r17 c9)
    (visited r17 c10)
    (visited r17 c11)
    (visited r17 c12)
    (visited r17 c13)
    (visited r17 c14)
    (visited r17 c15)
    (visited r17 c16)
    (visited r17 c17)
  )))
