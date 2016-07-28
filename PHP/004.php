<?php
	$ans = 0;
	for($i=100;$i<1000;$i++){
		for($j=100;$j<1000;$j++){
			$product = $i*$j;
			if(strcmp(strrev($product),$product) == 0){ // Awesome!
				if($product > $ans){
					$ans = $product;
				}
			}
		}
	}
	echo $ans;
?>