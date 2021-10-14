const assert = require('assert');
const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');
const stub = sinon.stub();

describe('Test Hooks', function() {
	let spyLog;
	beforeEach(function() {
		spyLog = sinon.spy(console, 'log');
	})

	afterEach(function() {
		spyLog.restore();
	})

	it('Test sendPaymentRequestToAPI for 120', function() {
		sendPaymentRequestToApi(100, 20);
		expect(spyLog.calledWith('The total is: 120')).to.be.true;
		expect(spyLog.calledOnce).to.be.true;
	})

	it('Test sendPaymentRequestToAPI for 20', function() {
		sendPaymentRequestToApi(10, 10);
		expect(spyLog.calledWith('The total is: 20')).to.be.true;
		expect(spyLog.calledOnce).to.be.true;
	})
})