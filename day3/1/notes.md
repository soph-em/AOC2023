Anything directly next to horizontally - *789
Anything directly above or below - find index of that array then look at index of array above or below
Anything diagonal - from symbol row above or below, index +/- 1


keep track of all the rows/indexes of special characters?


need 
467
35
633 
617 - doesn't re match
592
755 - finds '75'
664
598

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

<!-- all except 114, 58 -->

467 + 35 + 633 + 617 + 592 + 755 + 664 + 598