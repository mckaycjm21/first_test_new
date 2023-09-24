describe("Just testing knowledge of describe", function(){
  it('should calculate the monthly rate correctly', function () {
    const values = {
      amount: 15000,
      years: 10,
      rate: 5
    }
    expect(calculateMonthlyPayment(values)).toEqual('159.10')
  });
});

