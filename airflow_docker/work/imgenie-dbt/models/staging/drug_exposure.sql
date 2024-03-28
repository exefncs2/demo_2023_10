{{ config(materialized='table',
  depends_on=['ref("base_table_medicationstatement")']
  ,unique_key='drug_exposure_id') }}
select
'identifier' as "drug_exposure_id", --缺漏
'statusReason' as "stop_reason", --缺漏
"medicationReference" as "refills", --dispenseRequest.numberOfRepeatsAllowed 不存在
"medicationReference" as "quantity", --dispenseRequest.quantity 不存在
"medicationReference" as "days_supply", --dispenseRequest.expectedSupplyDuration 不存在
'medication' as "lot_number", --batch.lotNumber --缺漏
"medicationReference" as "sig", --dosageInstruction.text 不存在
"medicationReference" as "route_concept_id", --dosageInstruction.route 不存在
"medicationReference" as "provider_id", --requester.identifier 不存在
'context.identifier' as "visit_occurrence_id", --缺漏
'medication' as "drug_source_value", --缺漏
subject::json -> 'identifier' as "person_id", --缺漏
'medicationCodeableConcept' as "drug_concept_id", --缺漏
'effectivePeriod.low' as "drug_exposure_start_date", --缺漏
'effectivePeriod.low' as "drug_exposure_start_datetime", --缺漏
'effectivePeriod.high' as "drug_exposure_end_date", --缺漏
'effectivePeriod.high' as "drug_exposure_end_datetime", --缺漏
"medicationReference" as "verbatim_end_date" --validityPeriod.high --缺漏
,create_time
FROM 
  {{   ref('base_table_medicationstatement')  }}
