const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('Test calculateNumber', function(){
	it('Check sum positive and negative numbers', function() {
		assert.equal(calculateNumber(1,3), 4);
		assert.equal(calculateNumber(1, 3.7), 5);
		assert.equal(calculateNumber(1.2, 3.7), 5);
		assert.equal(calculateNumber(1.5, 3.7), 6);
		assert.equal(calculateNumber(-3.5, -6.7), -10);
	});
	it('Check if the args are numbers or if there are two args', function() {
		assert.equal(isNaN(calculateNumber()), true);
		assert.equal(isNaN(calculateNumber(9)), true);
		assert.equal(isNaN(calculateNumber('m')), true);
	});
});