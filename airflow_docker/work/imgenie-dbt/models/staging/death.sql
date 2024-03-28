{{ config(materialized='table',
  depends_on=['ref("base_table_adverseevent")']
  ,unique_key='person_id') }}
select --整篇無資料
'subject.identifier' as "person_id", --缺漏
'date' as "death_date", --缺漏
'date' as "death_datetime", --缺漏
'unknown' as "death_type_concept_id", --suspectedEntity.causality.extension : cdmh-pcornet-death-cause-source
'unknown' as "cause_concept_id" --suspectedEntity.causality.extension : cdmh-pcornet-death-cause, cdmh-pcornet-death-cause-code
,create_time
FROM 
  {{   ref('base_table_adverseevent')  }}
