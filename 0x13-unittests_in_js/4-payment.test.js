const assert = require('assert');
const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const stub = sinon.stub();

describe('Test Stubs', function() {
	const stubValue = sinon.stub(Utils, 'calculateNumber');
	const spyLog = sinon.spy(console, 'log');
	it('calls utils.calculateNumber', function() {
		stubValue.withArgs('SUM', 100, 20).returns(10);
		sendPaymentRequestToApi(100, 20);
		expect(spyLog.calledOnce).to.be.true;
		expect(spyLog.calledWith('The total is: 10')).to.be.true;
		stubValue.restore();
		spyLog.restore();
	})
})