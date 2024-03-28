{{ config(materialized='table',
  depends_on=['ref("base_table_composition")']
  ,unique_key='conditionid') }}
SELECT
 id as "conditionid",
 substring(subject from '"reference": "([^"]+)"') as "patid",
 substring(encounter from '"reference": "([^"]+)"') as "encounterid",
 'recordedDate' as "report_date", --缺漏 recordedDate
 'abatementDateTime' as "resolve_date", --缺漏 abatementDateTime
 'onsetDateTime' as "onset_date", --缺漏 onsetDateTime
 status as "condition_status", --名稱不同 clinicalStatus
 substring(section from '"code": "([^"]+)"') as "condition", --太多相同名稱 
 substring(section from '"display": "([^"]+)"') as "condition_type", --不知道取哪個 
 'unknown' as "condition_source" --不明 Condition.extension: cdmh-pcornet-condition-source
 ,create_time
FROM 
  {{ ref('base_table_composition') }}
