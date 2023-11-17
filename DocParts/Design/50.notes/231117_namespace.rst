AIGR/SIEVE Namespace analyse
============================

.. UML::

   @startuml
   skin rose
   skinparam style strictuml

   skinparam sequenceMessageAlign left


   actor Dev


   !procedure $register($ns, $n, $details=0)
       Dev -> $ns             : register($n)
      $ns o--\o $n : ""$ns._dict[$n]=$n""
       activate $ns

      !if $details
        group details
          $ns ->  $ns    : _register_2ways()
          $ns-> $n      : register_in_NS()
          $n o--\o $ns   :""$n._ns=$ns""
        end
      !else
          $ns-> $n      : register_in_NS()
          $n o--\o $ns   :""$n._ns=$ns""
      !endif
      deactivate $ns
   !endprocedure


   participant "simple_sieve :NS"  as simple_sieve    #LightSkyBlue
   participant "slow_start :NS"    as slow_start      #LightSkyBlue
   participant "SlowStart_1:P"     as SlowStart_1
   participant "SimpleSieve:P"     as SimpleSieve
   participant "SlowStart:P"       as SlowStart



   $register(simple_sieve, slow_start,1)
   $register(simple_sieve, SlowStart_1)
   $register(simple_sieve, SimpleSieve)
   @enduml
