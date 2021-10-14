const assert = require('assert');
const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('Test Spies', function() {
	const spyValue = sinon.spy(Utils, 'calculateNumber');
	it('calls utils.calculateNumber', function() {
		sendPaymentRequestToApi(100, 20);
		expect(spyValue.calledOnce).to.be.true;
		expect(spyValue.calledWith('SUM', 100, 20)).to.be.true;
		spyValue.restore();
	})
})