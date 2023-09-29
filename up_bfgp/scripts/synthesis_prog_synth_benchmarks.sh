python bfgp.py -d ../tests/domains/fibonacci/domain.txt \
               -i ../tests/domains/fibonacci/1.txt \
                  ../tests/domains/fibonacci/2.txt \
                  ../tests/domains/fibonacci/3.txt \
                  ../tests/domains/fibonacci/4.txt \
                  ../tests/domains/fibonacci/5.txt \
                  ../tests/domains/fibonacci/6.txt \
                  ../tests/domains/fibonacci/7.txt \
                  ../tests/domains/fibonacci/8.txt \
                  ../tests/domains/fibonacci/9.txt \
                  ../tests/domains/fibonacci/10.txt \
               -m synthesis \
               -t cpp \
               -l 7 \
               -f ed ilc \
               -o tmp_fibonacci/ \
               -p fibonacci

python bfgp.py -d ../tests/domains/find/domain.txt \
               -i ../tests/domains/find/1.txt \
                  ../tests/domains/find/2.txt \
                  ../tests/domains/find/3.txt \
                  ../tests/domains/find/4.txt \
                  ../tests/domains/find/5.txt \
                  ../tests/domains/find/6.txt \
                  ../tests/domains/find/7.txt \
                  ../tests/domains/find/8.txt \
                  ../tests/domains/find/9.txt \
                  ../tests/domains/find/10.txt \
               -m synthesis \
               -t cpp \
               -l 4 \
               -f ed ilc \
               -o tmp_find/ \
               -p find
               
python bfgp.py -d ../tests/domains/reverse/domain.txt \
               -i ../tests/domains/reverse/1.txt \
                  ../tests/domains/reverse/2.txt \
                  ../tests/domains/reverse/3.txt \
                  ../tests/domains/reverse/4.txt \
                  ../tests/domains/reverse/5.txt \
                  ../tests/domains/reverse/6.txt \
                  ../tests/domains/reverse/7.txt \
                  ../tests/domains/reverse/8.txt \
                  ../tests/domains/reverse/9.txt \
                  ../tests/domains/reverse/10.txt \
               -m synthesis \
               -t cpp \
               -l 7 \
               -f ed ilc \
               -o tmp_reverse/ \
               -p reverse
               
python bfgp.py -d ../tests/domains/select/domain.txt \
               -i ../tests/domains/select/1.txt \
                  ../tests/domains/select/2.txt \
                  ../tests/domains/select/3.txt \
                  ../tests/domains/select/4.txt \
                  ../tests/domains/select/5.txt \
                  ../tests/domains/select/6.txt \
                  ../tests/domains/select/7.txt \
                  ../tests/domains/select/8.txt \
                  ../tests/domains/select/9.txt \
                  ../tests/domains/select/10.txt \
               -m synthesis \
               -t cpp \
               -l 7 \
               -f ed ilc \
               -s 1 \
               -o tmp_select/ \
               -p select
               
python bfgp.py -d ../tests/domains/sorting/domain.txt \
               -i ../tests/domains/sorting/1.txt \
                  ../tests/domains/sorting/2.txt \
                  ../tests/domains/sorting/3.txt \
                  ../tests/domains/sorting/4.txt \
                  ../tests/domains/sorting/5.txt \
                  ../tests/domains/sorting/6.txt \
                  ../tests/domains/sorting/7.txt \
                  ../tests/domains/sorting/8.txt \
                  ../tests/domains/sorting/9.txt \
                  ../tests/domains/sorting/10.txt \
               -m synthesis \
               -t cpp \
               -l 8 \
               -f ed ilc \
               -o tmp_sorting/ \
               -p sorting                                             
               
python bfgp.py -d ../tests/domains/triangular_sum/domain.txt \
               -i ../tests/domains/triangular_sum/1.txt \
                  ../tests/domains/triangular_sum/2.txt \
                  ../tests/domains/triangular_sum/3.txt \
                  ../tests/domains/triangular_sum/4.txt \
                  ../tests/domains/triangular_sum/5.txt \
                  ../tests/domains/triangular_sum/6.txt \
                  ../tests/domains/triangular_sum/7.txt \
                  ../tests/domains/triangular_sum/8.txt \
                  ../tests/domains/triangular_sum/9.txt \
                  ../tests/domains/triangular_sum/10.txt \
               -m synthesis \
               -t cpp \
               -l 5 \
               -f ed ilc \
               -o tmp_triangular_sum/ \
               -p triangular_sum
               
               
