# -*- coding: utf-8 -*-
import hashlib
import time
import json

class BCHMerchantInsuranceActuary:
    def __init__(self, token_category: str = "bch_ins_category_77"):
        self.token_category = token_category

    def issue_merchant_protection_token(self, merchant_id: str, monthly_turnover_bch: float) -> dict:
        premium_bch = monthly_turnover_bch * 0.008
        policy_hash = hashlib.sha256(f"{merchant_id}:{monthly_turnover_bch}:{time.time()}".encode()).hexdigest()[:16]
        return {
            "policy_id": f"BCH-POL-{policy_hash}",
            "merchant_id": merchant_id,
            "cashtoken_category": self.token_category,
            "monthly_turnover_bch": monthly_turnover_bch,
            "premium_bch": round(premium_bch, 4),
            "zero_conf_protection": True,
            "bip21_payment_uri": f"bitcoincash:{merchant_id}?amount={round(premium_bch, 4)}",
            "timestamp": int(time.time())
        }

if __name__ == "__main__":
    actuary = BCHMerchantInsuranceActuary()
    res = actuary.issue_merchant_protection_token("bitcoincash:qpm2qsznhks23z7629mms6s4cwef74vcwvy22gdx6a", 12.5)
    print("BCH Merchant Insurance Policy:", json.dumps(res, indent=2))
