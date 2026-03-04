function Calculator_Mortgage(Loan_Amount, Loan_Term) {
  let P = Loan_Amount;
  const r = 0.045 / 12;
  let n = Loan_Term * 12;
  let result = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1);
  return result;
}

let form_input = document
  .getElementById("action")
  .addEventListener("submit", function (process) {
    process.preventDefault();
    let Loan_Amount = parseInt(document.getElementById("amount").value);
    let Loan_Term = parseInt(document.getElementById("term").value);
    let monthly = parseInt(document.getElementById("income").value);
    let threshold = 0.3 * monthly;
    let Monthly_Payment = Calculator_Mortgage(Loan_Amount, Loan_Term);
    let Total_Payment = Monthly_Payment * (Loan_Term * 12);
    let Total_Interest = Total_Payment - Loan_Amount;
    let Income_Left = monthly - Monthly_Payment;
    if (threshold <= Calculator_Mortgage(Loan_Amount, Loan_Term)) {
      $("#check").html(
        "<span style = 'color:red'> Loan denied: Monthly payment exceeds 30% of your income."
      );
    } else {
      $("#check").html(
        "<span style = 'color:green'> Loan Approved <br>" +
          "Monthly Payment = " +
          Monthly_Payment.toFixed(2) +
          "<br>" +
          "Total Payment = " +
          Total_Payment.toFixed(2) +
          "<br>" +
          "Total Interest = " +
          Total_Interest.toFixed(2) +
          "<br>" +
          "Income Left = " +
          Income_Left.toFixed(2)
      );
    }
  });
