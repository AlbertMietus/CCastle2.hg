AIGR/SIEVE Namespace analyse
============================

.. uml::

   @startuml
   skin rose
   'skinparam style strictuml
   skinparam sequenceMessageAlign left

   actor Dev
   entity T_Protocol
   boundary "CastleMacros.jinja2" as m

   !procedure $register($ns, $n, $details=0)
       Dev -> $ns             : register($n)
      $ns o--\o $n : ""$ns._dict[$n] := $n""
       activate $ns

      !if $details
        group details
          $ns ->  $ns    : _register_2ways()
          $ns-> $n      : register_in_NS()
        end
          $n o--\o $ns   :""$n._ns := $ns""
      !else
          $n o--\o $ns   :""$n._ns := $ns""
      !endif
      deactivate $ns
   !endprocedure


   participant "simple_sieve :NS"  as simple_sieve    #LightSkyBlue
   participant "slow_start :NS"    as slow_start      #LightSkyBlue
   participant "SimpleSieve:P"     as SimpleSieve
   participant "SlowStart_1:P"     as SlowStart_1
   participant "SlowStart:P"       as SlowStart

   == TestDoubles/AIGR/sieve/namespaces.py ==

   $register(simple_sieve, slow_start,1)
   alt "old AIGR"
     $register(simple_sieve, SlowStart_1)
   else "deleted 'simple_sieve.register(protocols.SlowStart_1)'"
     note over simple_sieve, SlowStart1 #aqua: Is it a hack? Should it be in RenderNS (ToDo), or ...
   end
   $register(simple_sieve, SimpleSieve)
   $register(slow_start, SlowStart)

   == pytst/writers/RPy/test_3_SieveProtocols.py==


   [-> T_Protocol: render((sieve.SlowStart_1, sieve.SimpleSieve))
   note left: ""inherit_from={{proto.based_on.ns.name}}.{{m.ProtocolName(proto.based_on)}}""

   ... sieve.SlowStart_1 ...
   T_Protocol -> SlowStart_1: based_on()
   SlowStart_1 o/--x SlowStart: "".based_on""
   T_Protocol <-- SlowStart_1: SlowStart

   T_Protocol ->  SlowStart: ns()
   T_Protocol <-- SlowStart: slow_start

   opt "obj 2 str"
      T_Protocol -> slow_start :name
      T_Protocol <-- slow_start : "slow_start"
   end

   T_Protocol -> m: ProtocolName(SlowStart)
   T_Protocol <--m: ""cc_P_Slowstart""
   note right:   cc_P_{{Proto.name}}
   note left of T_Protocol: inherit_from=slow_start.cc_P_SlowStart

   ... sieve.SimpleSieve ...
   T_Protocol -> SimpleSieve: based_on()
   SimpleSieve o/--x SlowStart_1: "".based_on""
   T_Protocol <-- SimpleSieve: SlowStart_1

   T_Protocol ->  SlowStart_1: ns()
   alt "old AIGR"
      T_Protocol <-- SlowStart_1: simple_sieve
      note left: Note: ‘simple_sieve’ is (also) is the current namespace\n\tSo, it should be named

      opt "obj 2 str"
         T_Protocol ->   simple_sieve : name
         T_Protocol <--  simple_sieve : "<color:red>simple_sieve</color>"
      end

      T_Protocol -> m: ProtocolName(SimpleSieve)
      T_Protocol <--m: ""cc_P_SimpleSieve""
      note right:   cc_P_{{Proto.name}}

      note left of T_Protocol #orangered: <color:yellow>inherit_from=<color:white>simple_sieve.<color:yellow>cc_P_SimpleSieve
   else "deteled 'simple_sieve.register(protocols.SlowStart_1)'"
      T_Protocol <-- SlowStart_1: <NIL>

      T_Protocol -> m: ProtocolName(SimpleSieve)
      T_Protocol <--m: ""cc_P_SimpleSieve""

      note left of T_Protocol #lime: <color:white>inherit_from=cc_P_SimpleSieve</color>
   end

   @enduml

