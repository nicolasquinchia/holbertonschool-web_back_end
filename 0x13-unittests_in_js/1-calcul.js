module.exports = function calculateNumber(type, a, b) {
	let num_a = Math.round(a);
	let num_b = Math.round(b);

	switch (type) {
		case 'SUM':
			return num_a + num_b;
			break;
		case 'SUBTRACT':
			return num_a - num_b;
			break;
		case 'DIVIDE':
			if (num_b === 0) {
				return 'Error';
				break;
			}
			return num_a / num_b;
			break;
	}
}