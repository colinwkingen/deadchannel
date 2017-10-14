$(document).ready(function() {
	function generateColor() {
		console.log("Generating...");
		var randomColor = "#";
		var hexArr = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
		for (i=0;i<6;i++) {
			var index = Math.floor(Math.random()*15);
			randomColor+= hexArr[index];
		}
		return randomColor;
	}
		
	function randomBrickColor() {
			setTimeout(function(){
				var color = generateColor();
				$('.letter_block').css('background-color',generateColor());
				console.log('Color: '+color);
				randomBrickColor();
			},randomTimer());
	}
	
	function randomTimer() {
		return Math.floor(Math.random()*5000);
	}
	randomBrickColor();
	
});