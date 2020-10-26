let generate = https://prelude.dhall-lang.org/List/generate

let buildGroup = \(index : Natural) ->
 "ИКБО-${Natural/show (index + 1)}-19"

let groups = generate 24 Text buildGroup

let makeStudent =
 \(age : Natural) ->
 \(group : Natural) ->
 \(name : Text) ->
  { age = age
  , group = "ИКБО-${Natural/show group}-19"
  , name = name
  }

let students =
 [ makeStudent 19 4 "Иванов И.И."
 , makeStudent 18 5 "Петров П.П."
 , makeStudent 18 5 "Сидоров С.С."
 , makeStudent 19 1 "Ворожейкин Д.А."
 ]

let subject = "Конфигурационное управление"
in {groups, students, subject}