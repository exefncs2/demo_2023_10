{{ config(materialized='table',
  depends_on=['ref("base_table_condition")']
  ,unique_key='condition_occurrence_id') }}
SELECT
'identifier' as "condition_occurrence_id", --缺漏 identifier
'identifier' as "condition_occurrence_source_value", --缺漏 identifier
'unknown' as "provider_id", --缺漏 asserter.identifier
--(json_array_elements(asserter::json) -> 'identifier' ) as "provider_id", 
'unknown' as "visit_occurrence_id", --缺漏 encounter.identifier
--(json_array_elements(encounter::json) -> 'identifier' ) as "visit_occurrence_id",
category as "condition_status_concept_id",
subject::json -> 'identifier'  as "person_id", --缺漏 subject.identifier
substring(code from '"code": "([^"]+)"') as "condition_concept_id", --code
substring(code from '"display": "([^"]+)"') as "condition_source_value", --code
'unknown' as "condition_start_date", -- onset[x]
'unknown' as "condition_start_datetime", -- onset[x]
'unknown' as "condition_end_date", -- abatement[x]
'unknown' as "condition_end_datetime", -- abatement[x]
'unknown' as "condition_type_concept_id", --Condition.code.extension : cdmh-pcornet-condition-source1
'unknown' as "condition_type_source_value", --Condition.code.extension : cdmh-pcornet-condition-source1
substring(note from '"text": "([^"]+)"') as "stop_reason"
,create_time
FROM 
  {{ ref('base_table_condition') }}


-- onset[x]
-- .... onsetDateTime
-- .... onsetAge
-- .... onsetPeriod
-- .... onsetRange	
-- .... onsetString

-- abatement[x]
-- .... abatementDateTime
-- .... abatementAge
-- .... abatementPeriod			
-- .... abatementRange			
-- .... abatementString			
