<?php
	$maximum = 4000000;
	$fib[1]=1;
	$fib[2]=1;
	for($i=3;;$i++){
		$fib[$i]=$fib[$i-1]+$fib[$i-2];
		if($fib[$i] > $maximum){
			break;
		}
		if($fib[$i]%2 == 0){
			$sum += $fib[$i];
		}
	}
	echo $sum;
?>