const assert = require('assert');
const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('Test calculateNumber', function() {
	it('Check operations with SUM', function() {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        expect(calculateNumber('SUM', 5, 3)).to.equal(8);
        expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
	});
	it('Check operations with SUBTRACT', function() {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
        expect(calculateNumber('SUBTRACT', 10.2, 7.6)).to.equal(2);
	});
	it('Check operations with DIVIDE', function() {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        expect(calculateNumber('DIVIDE', 5, 2)).equal(2.5);
        expect(calculateNumber('DIVIDE', 18.2, 5.7)).to.equal(3);
	});
    it('Check DIVIDE Error', function() {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 10, 0)).to.equal('Error');
    });
    it('Check for NaN or invalid Arguments', function() {
        expect(isNaN(calculateNumber(1, 2))).to.equal(true);
        expect(isNaN(calculateNumber('SUM', 2))).to.equal(true);
        expect(isNaN(calculateNumber(5))).to.equal(true);
        expect(isNaN(calculateNumber('DIVIDE'))).to.equal(true);
        expect(isNaN(calculateNumber())).to.equal(true);
    });
})