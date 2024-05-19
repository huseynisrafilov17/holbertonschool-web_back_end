/* eslint no-underscore-dangle: 0 */
import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._currency = currency;
    this._amount = amount;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = value;
  }

  displayFullPrice() {
    return `${this.amount} ${this.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
