
import requests
import logging

API_URL = 'http://localhost:3000/random'
logging.basicConfig(filename="loan_decisions.log", level=logging.INFO, format="%(asctime)s - %(message)s")

class LoanApprovalSystem:
    """Loan Approval System"""

    def fetch_credit_score(self):
        """Fetch credit score from API"""
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            if response.content:
                try:
                    data = response.json()
                    return data.get("creditScore")
                except ValueError as e:
                    logging.error("Failed to parse JSON response: %s", e)
                    return None
            else:
                logging.error("API response is empty")
                return None
        except requests.exceptions.RequestException as e:
            logging.error("API call failed with error: %s", e)
            return None

    def evaluate_credit_score(self, score):
        """Determine loan approval based on credit score"""
        if score is None:
            return "Error: No valid credit score retrieved"
        if score >= 700:
            return "Approved"
        elif score < 500:
            return "Rejected"
        else:
            return "Flagged for human review"

    def process_loan(self):
        """Fetch, evaluate, process loan decision"""
        credit_score = self.fetch_credit_score()
        #print(credit_score)
        if credit_score is not None:
            decision = self.evaluate_credit_score(credit_score)
            print(f"Credit score: {credit_score}, Decision: {decision}")
            logging.info("Credit score: %s | Decision: %s", credit_score, decision)
            if decision == "Flagged for human review":
                human_decission = input("Enter '1' to approve or '0' to reject: ").strip()
                if human_decission == '1':
                    final_decision = "Approved"
                elif human_decission == '0':
                    final_decision = "Rejected"
                else:
                    final_decision = "Invalid input"
                print(f"Final Decision: {final_decision}")
                logging.info("Final Decision: %s", final_decision)
        else:
            print('Failed to retrieve credit score')

if __name__ == "__main__":
    loan = LoanApprovalSystem()
    loan.process_loan()


