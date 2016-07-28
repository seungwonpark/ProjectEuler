<?php
	$val = 600851475143; // overflow. I must use GMP.
	echo $val;
	echo "<br/>";
	for($i=3;;$i+=2){
		if($i*$i > $val){
			echo $val;
			break;
		}
		while($val%$i == 0){
			$val /= $i;
		}
	}
?>