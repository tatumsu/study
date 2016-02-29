class InternalRole < ActiveRecord::Base
end

manager = InternalRole.create
manager.name = "Fleet Manager"
