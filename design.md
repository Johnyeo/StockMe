<people>
=================================================================
Stephen $10     risk preference 50%
Susan   $10     risk preference 100%
John    $10     risk preference 100%
Alex    $5      risk preference 100%
Lisa    $5      risk preference 100%

<companies>
=================================================================
IBM     5      $5/s
Apple   5      $5/s
Google  5      $5/s

********************************************************************************************

Stephen     $10
=================================================================
rate    IBM     5
        Apple   1
        Google  -1
------------------------------------------
buy     IBM     50%(risk preference)    $5      1 share
sell    none

Susan       $10
=================================================================
rate    IBM     5
        Apple   1
        Google  -1
------------------------------------------
buy     IBM     100%(risk preference)    $10      2 share
sell    none

John        $10
=================================================================
rate    IBM     5
        Apple   1
        Google  -1
------------------------------------------
buy     IBM     100%(risk preference)    $10      2 share
sell    none

Alex        $5
=================================================================
rate    IBM     5
        Apple   1
        Google  -1
------------------------------------------
buy     IBM     100%(risk preference)    $5      1 share   fail
sell    none

lisa        $5
=================================================================
rate    IBM     5
        Apple   1
        Google  -1
------------------------------------------
buy     IBM     100%(risk preference)    $5      1 share   fail
sell    none

********************************************************************************************

<people>
=================================================================
Stephen $10
Susan   $10
John    $10
Alex    $5
Lisa    $5

<companies>
=================================================================
IBM     -4      -(-4/5-1)* $5/s = $9/s
Apple   5       -(5/5-1)* $5/s = $0/s  --> $1/s  this company is out if it's 0. but for test, we set a limit of fluctate, say 80%
Google  5       -(5/5-1)* $5/s = $0/s  --> $1/s
------------------------------------------

<people>
=================================================================
Stephen $5     risk preference 50%
Susan   $0     risk preference 100%
John    $0     risk preference 100%
Alex    $5      risk preference 100%
Lisa    $5      risk preference 100%

Stephen     $5  -- +3.6$ -3$ = 5.6
=================================================================
rate    IBM     -1
        Apple   0
        Google  3
------------------------------------------
buy     Google  50%(risk preference)*60% (expection) = 30%    $3    3share
sell    IBM     20% (expection) = 20%    0.4 share   -> $9*0.4 = $3.6


Susan       $0
=================================================================
rate    IBM     2
        Apple   1
        Google  -1
------------------------------------------
buy     none
sell    none

John        $0
=================================================================
rate    IBM     -4
        Apple   1
        Google  0
------------------------------------------
buy     Apple   100%(risk preference) * 20%(expection) = 20%      $1   1share
sell    IBM     80%(expections) = 80%     0.8 share   --->$9*0.4 = $3.6

Alex        $5
=================================================================
rate    IBM     1
        Apple   0
        Google  3
------------------------------------------
buy     Google     100%(risk preference)*60%    $3      3 share
sell    none

lisa        $5
=================================================================
rate    IBM     0
        Apple   2
        Google  -1
------------------------------------------
buy     Apple     100%(risk preference) * 2/5 (rise expection)    $2  2share
sell    none

********************************************************************************************

<companies>
=================================================================
IBM     -4      -(-4/5-1)* $5/s = $9/s
Apple   5       -(5/5-1)* $5/s = $0/s  --> $1/s  this company is out if it's 0. but for test, we set a limit of fluctate, say 80%
Google  5       -(5/5-1)* $5/s = $0/s  --> $1/s
------------------------------------------

<people>
=================================================================
Stephen $5     risk preference 50%
Susan   $0     risk preference 100%
John    $0     risk preference 100%
Alex    $5      risk preference 100%
Lisa    $5      risk preference 100%

