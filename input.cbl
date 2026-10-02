           identification division.
           program-id. input-test.

           procedure division.

           main-procedure.
               display "hello world" at 0505
               display "hello world" line 06 column 05

               display "hello world"
                   line 09 column 05
                   with bell
               end-display
               goback.

           end program input-test.
