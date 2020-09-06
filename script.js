window.onload = function() {
	let top = document.getElementsByClassName('top')[0];
	let startBtn = document.getElementsByClassName('start')[0];
	let clickBtn = document.getElementsByClassName('click')[0];
	let standbyCount = document.getElementsByClassName('standby-count')[0];
	let result = document.getElementsByClassName('result')[0];
	let timeD = document.getElementsByClassName('time')[0];
	let clickNumD = document.getElementsByClassName('click-num')[0];
	let clickPerNumD = document.getElementsByClassName('click-per-num')[0];
	let resetBtn = document.getElementsByClassName('reset')[0];


	let count = document.createElement('h2');
	let sec = 3;
	count.innerHTML = sec;
	standbyCount.appendChild(count);

	let clickNumber = 0;


	startBtn.onclick = function() {
		top.style.display = 'none';

		let countDown = setInterval(
			function() {
				count.innerHTML -= 1;
				if(count.innerHTML == 0) {
					clearInterval(countDown);
					main();
				}
			}, 1000)
	}

	function main() {
		clickBtn.style.cursor = 'pointer';
		clickBtn.onclick = function() { clickNumber++ }

		let selectedNumber = new Number(document.getElementsByClassName('select-time')[0].value);
		count.innerHTML = selectedNumber.toFixed(2);
		
		let countDown = setInterval(
			function() {
				count.innerHTML = (count.innerHTML - 0.01).toFixed(2);
				if(count.innerHTML == 0) {
					clearInterval(countDown);
					displayResult(selectedNumber);
				}
			}, 1);
	}

	function displayResult(select) {
		clickBtn.style.cursor = 'default';
		timeD.innerHTML = select + '秒';
		clickNumD.innerHTML = clickNumber + '回';
		clickPerNumD.innerHTML = (clickNumber / select).toFixed(2) + '回';
		result.style.display = 'block';
	}

	resetBtn.onclick = function() {
		top.style.display = 'block';
		result.style.display = 'none';
		count.innerHTML = sec;
		clickNumber = 0;
		timeD.innerHTML = '';
		clickNumD.innerHTML = '';
		clickPerNumD.innerHTML = '';
	}
}
