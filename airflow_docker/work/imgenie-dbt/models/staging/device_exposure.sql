{{ config(materialized='table',
  depends_on=['ref("base_table_procedure")']
  ,unique_key='device_exposure_id') }}
SELECT
'focalDevice.udiCarrier' as "device_exposure_id", --缺漏
'performer.actor' as "provider_id", --缺漏
'encounter.identifier' as "visit_occurrence_id", --缺漏
subject::jsonb -> 'reference'  as "person_id", --缺漏 'identifier'
'performedPeriod.low' as "device_exposure_start_date", --缺漏
'performedPeriod.low' as "device_exposure_start_datetime", --缺漏
'performedPeriod.high' as "device_exposure_end_date", --缺漏
'performedPeriod.high' as "device_exposure_end_datetime", --缺漏
'focalDevice.manipulated.type , Procedure.usedReference.type' as "device_type_concept_id", --缺漏 兩個來源?
'focalDevice.manipulated.udiCarrier , Procedure.usedReference.udiCarrier' as "unique_device_id" --缺漏 兩個來源?
,create_time
FROM 
  {{   ref('base_table_procedure')  }}
