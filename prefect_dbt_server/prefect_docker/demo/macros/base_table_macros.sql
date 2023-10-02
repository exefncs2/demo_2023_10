{% macro base_table(resource_type_value) %}
{{ config(materialized='view',
  depends_on=[var('myorigin'),var('myrow_data')])
   }}

{% set table_name  =  ref(var('myrow_data')) %}

    {% set columns_query = run_query(
        "SELECT DISTINCT column_name FROM " ~ table_name ~ " " ~
        "WHERE row IN (SELECT DISTINCT row FROM " ~  table_name ~ " " ~
        "WHERE column_name = 'resourceType' AND column_value = '" ~ resource_type_value ~ "')"
    ) %}
    
    SELECT
        {% for column_name in columns_query %}
          (SELECT column_value FROM {{ table_name }} WHERE column_name = '{{ column_name.column_name }}' AND row = main.row) AS "{{ column_name.column_name }}"
          {% if not loop.last %},{% endif %}
        {% endfor %}
    FROM {{ table_name }} main
    WHERE column_name = 'resourceType' AND column_value = '{{ resource_type_value }}'
{% endmacro %}
