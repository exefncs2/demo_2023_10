{{ config(materialized='incremental',
  depends_on=['ref("base_table_practitioner")']
  ,unique_key='provider_id'
  ,tags=['provider']
  ) 
   }}
    SELECT 
        SUBSTRING(meta FROM '"source": "([^"]+)"') AS provider_id, --不知道取哪個
        JSONB_ARRAY_ELEMENTS(name::JSONB) ->> 'text' AS provider_name,
        SUBSTRING(identifier FROM '"npi": "([^"]+)"') AS npi, --不知道取哪個
        'qualification' AS dea, --缺漏
        'specialty' AS specialty_concept_id, --缺漏
        'location' AS care_site_id, --缺漏
        'birthDate' AS year_of_birth, --缺漏
        'gender' AS gender_concept_id, --缺漏
        create_time
    FROM 
        {{ ref('base_table_practitioner') }}

{% if is_incremental() %}
where create_time > (SELECT MAX(create_time) FROM {{ this }} LIMIT 1)
{% endif %}