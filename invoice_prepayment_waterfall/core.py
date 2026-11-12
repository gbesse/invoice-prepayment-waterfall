from decimal import Decimal,InvalidOperation,ROUND_HALF_UP,localcontext
from .common import identifier,unique_ids,integer
def decimal(x):
 if not isinstance(x,str)or len(x)>80:raise ValueError('decimal_string')
 try:v=Decimal(x)
 except InvalidOperation as e:raise ValueError('decimal')from e
 if not v.is_finite()or abs(v)>Decimal('1e12'):raise ValueError('decimal_range')
 return v
def money(x):
 v=decimal(x)
 if v<0 or v!=v.quantize(Decimal('.01')):raise ValueError('minor_unit')
 return v
def run(data):
 total=money(data['invoice_total']);currency=identifier(data['currency']);payments=data['prepayments']
 if not isinstance(payments,list)or len(payments)>10000:raise ValueError('payments')
 unique_ids(payments);balance=total;surplus=Decimal(0);out=[]
 for p in payments:
  if p.get('currency',currency)!=currency:raise ValueError('mixed_currency')
  amount=money(p['amount']);applied=min(balance,amount);balance-=applied;surplus+=amount-applied
  out.append({'id':p['id'],'applied':str(applied.quantize(Decimal('.01'))),'unallocated':str((amount-applied).quantize(Decimal('.01'))),'remaining_invoice_balance':str(balance.quantize(Decimal('.01')))})
 return {'currency':currency,'allocations':out,'balance':str(balance.quantize(Decimal('.01'))),'unallocated_prepayment':str(surplus.quantize(Decimal('.01'))),'payment_executed':False}
