const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('Test calculateNumber', function() {
	it('Check operations with SUM', function() {
        assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.equal(calculateNumber('SUM', 5, 3), 8);
        assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
	});
	it('Check operations with SUBTRACT', function() {
        assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.equal(calculateNumber('SUBTRACT', 5, 3), 2);
        assert.equal(calculateNumber('SUBTRACT', 10.2, 7.6), 2);
	});
	it('Check operations with DIVIDE', function() {
        assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.equal(calculateNumber('DIVIDE', 5, 2), 2.5);
        assert.equal(calculateNumber('DIVIDE', 18.2, 5.7), 3);
	});
    it('Check DIVIDE Error', function() {
        assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        assert.equal(calculateNumber('DIVIDE', 10, 0), 'Error');
    });
    it('Check for NaN or invalid Arguments', function() {
        assert.equal(isNaN(calculateNumber(1, 2)), true);
        assert.equal(isNaN(calculateNumber('SUM', 2)), true);
        assert.equal(isNaN(calculateNumber(5)), true);
        assert.equal(isNaN(calculateNumber('DIVIDE')), true);
        assert.equal(isNaN(calculateNumber()), true);
    });
})